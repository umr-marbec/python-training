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

# # Changing default Matplotlib settings
#
# In order to change the default Matplotlib settings (for instance default colors, default linewidth, etc.), the user needs to modify the values of the `matplotlib.pyplot.rcParams` dictionary.
#
# For a detailed description of all the customizarion methods, visisit [matplotlib](https://matplotlib.org/3.1.3/tutorials/introductory/customizing.html) webpage.

# +
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 200)
y = [np.cos(x), np.sin(x), np.cos(2*x), np.cos(x/2.)]
y = np.array(y).T
# -

plt.figure()
plt.plot(x, y)
plt.show()

# ## In a script
#
# If the user wants to change the default values only within a given script, this is done as follows:

from cycler import cycler  # used to define color cycles
plt.rcParams['lines.linewidth'] = 5
plt.rcParams['axes.prop_cycle'] = cycler('color', ['darkorange', 'plum', 'gold'])
plt.figure()
plt.plot(x, y)
plt.show()

# ## Changing the parameters for all sessions
#
# Default matplotlib parameters are stored in a 
# [matplotlibrc](https://matplotlib.org/3.1.3/tutorials/introductory/customizing.html#the-matplotlibrc-file) configuration file. Python will search this file into 3 different locations in the following order order:
#
# 1. in the current working directory (usually used for specific customizations that you do not want to apply elsewhere)
# 2. `$MATPLOTLIBRC` if it is a file, else `$MATPLOTLIBRC/matplotlibrc`
# 3. On `.config/matplotlib/matplotlibrc` (Linux) or `.matplotlib/matplotlibrc` (other platforms)
#
# If no `matplotlibrc` file is found, then the default value will be used. The path of the `matplotlibrc` file that is used in a given session can be obtained by using the `matplotlib_fname` method.

print(mpl.matplotlib_fname())

# To change your Matplotlib default parameters, download the [sample matplotlibrc](https://matplotlib.org/3.1.3/tutorials/introductory/customizing.html#matplotlibrc-sample) file and put it in any of the three directories described above.
#
# Then, uncomment the lines you are interested in and change the values.
