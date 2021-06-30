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
# ### Conda virtual environments
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
# Libraries are loaded by using the `import` statement. It can be done as follows:

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

print(numpy.mean([0, 1, 2], keepdims=True)) # 2 arguments provided
print(mp.is_interactive())  # no argument

# To get some help about a function, use the `help` function:

help(mp.is_interactive)

# ### Bad practice!
#
# Libraries can also be loaded as follows:

# +
# loading the DataFrame function of the pandas lib.
from pandas import DataFrame
print(DataFrame) # no pandas.DataFrame in this case

# loading all the objects of the stats module
from scipy.stats import *
print(randint)
# -

# In this case, part or all the content of the modules is stored in the current namespace.
#
# <div class="alert alert-danger">
#     <strong>Warning!</strong> I strongly recommend to <strong>never</strong> use this way of importing modules, since they may be in conflict with other objects.
# </div>

# +
import numpy as np
x = np.array([1e4, 1e6])

from numpy import *
print(log10(x))
from math import *
# print(log10(x))  will fail
# -

# Here, the `numpy.log10` method has been overwritten by the `math.log10` one.
#
# ### Loading your libraries
#
# If you want to load your own function, stored in a `mylib.py` file, you first need to add your library directory to the `PYTHONPATH`. At the beginning of your script, add:
#
# ```
# import sys
# sys.path.append('/add/other/directory/')
# import mylib
# ```
#
# **When the PYTHONPATH is modified this way, it is only valid for the current Python script.**
#
# In order to change the Python default paths, you need to create a `PYTHONPATH` environment variable. With Mac Os X/Linux, edit your `.bashrc` or `.cshrc` file and add:
#
# ```
# # bashrc
# export PYTHONPATH=${PYTHONPATH}:/add/other/directory
# # cshrc
# setenv PYTHONPATH /add/other/directory:${PYTHONPATH}
# ```
#
# In Windows, see for instance [oracle.com](https://docs.oracle.com/en/database/oracle/r-enterprise/1.5.1/oread/creating-and-modifying-environment-variables-on-windows.html#GUID-DD6F9982-60D5-48F6-8270-A27EC53807D0)
#
#
